"""Components are the basic building blocks of systems.

This module contains the definition of Components, and the implementation of
functionality to create them.
"""

import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from numerous.grpc.spm_pb2_grpc import FileManagerStub

from numerous.sdk.models.input import (
    InputSource,
    InputVariable,
    InputVariableScenarioSource,
    InputVariableStaticSource,
)
from numerous.sdk.models.parameter import Parameter, get_parameters_dict

log = logging.getLogger(__name__)


@dataclass
class SubComponentNotFound(Exception):
    """Raised when creating a :class:`Component` is configured with a subcomponent that
    does not exist.
    """

    component_uuid: str


@dataclass
class Component:
    """A component of a :class:`~numerous.sdk.models.scenario.Scenario`, containing
    parameters, input variables, and any subcomponents."""

    uuid: str
    id: str
    type: str
    name: str
    item_class: list[str]
    is_enabled: bool
    is_main: bool
    input_variables: dict[str, InputVariable]
    components: dict[str, list["Component"]]
    parameters: dict[str, Parameter]
    is_dummy: bool = False
    """The subcomponents of this component."""

    @staticmethod
    def from_document(
        path: list[str],
        component: dict[str, Any],
        all_components: list[dict[str, Any]],
        input_sources_mapping: dict[str, InputSource],
        file_manager_client: FileManagerStub,
    ) -> "Component":
        component_path = path + [component["name"]]
        return Component(
            uuid=component["uuid"],
            id=component["id"],
            type=component["type"],
            name=component["name"],
            is_enabled=not bool(component["disabled"]),
            is_main=bool(component["isMainComponent"]),
            components=_extract_subcomponents(
                component_path,
                component,
                all_components,
                input_sources_mapping,
                file_manager_client,
            ),
            item_class=component["item_class"].split("."),
            input_variables=_extract_input_variables(
                component_path, component, input_sources_mapping
            ),
            parameters=get_parameters_dict(
                component.get("parameters", []), file_manager_client
            ),
        )


def _extract_subcomponents(
    path: list[str],
    component: dict[str, Any],
    all_components: list[dict[str, Any]],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client: FileManagerStub,
) -> dict[str, list[Component]]:
    subcomponents = defaultdict(list)
    for subcomponent_ref in component.get("subcomponents", []):
        subcomponents[subcomponent_ref["name"]].append(
            _extract_subcomponent(
                path,
                subcomponent_ref["uuid"],
                all_components,
                input_sources_mapping,
                file_manager_client,
            )
        )
    return subcomponents


def _extract_subcomponent(
    path: list[str],
    subcomponent_uuid: str,
    all_components: list[dict[str, Any]],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client: FileManagerStub,
) -> Component:
    subcomponent = next(
        (
            subcomponent
            for subcomponent in all_components
            if subcomponent.get("uuid") == subcomponent_uuid
        ),
        None,
    )

    if subcomponent is None:
        raise SubComponentNotFound(component_uuid=subcomponent_uuid)

    return Component.from_document(
        path,
        subcomponent,
        all_components,
        input_sources_mapping=input_sources_mapping,
        file_manager_client=file_manager_client,
    )


def extract_components(
    data: dict[str, Any],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client,
) -> dict[str, Component]:
    extracted_sim_components = _extract_sim_components(
        data, input_sources_mapping, file_manager_client
    )
    generated_dummy_components = _generate_dummies_components_in_containers(data)
    components = {**generated_dummy_components, **extracted_sim_components}
    return components


def _extract_sim_components(
    data: dict[str, Any],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client,
) -> dict[str, Component]:
    components = data.get("simComponents", [])
    subcomponent_uuids = _get_all_subcomponent_uuids(components)
    return {
        component["name"]: Component.from_document(
            [], component, components, input_sources_mapping, file_manager_client
        )
        for component in components
        if component["uuid"] not in subcomponent_uuids
    }


def _generate_dummies_components_in_containers(
    data: dict[str, Any],
) -> dict[str, Component]:
    # Check if system is initialized. If not, issue a warning.
    if "system" not in data:
        log.warning(
            "Detected scenario not saved. It is not possible to access container components before saving the scenario"
        )
        return {}

    sim_components: list[dict[str, Any]] = data.get("simComponents", [])
    component_types = data["system"].get("componentTypes", [])
    component_types_ids = [component_type["id"] for component_type in component_types]

    dummy_components: dict[str, Component] = {}
    for container in data["system"].get("containers", []):
        sim_component_ids_with_matching_container_id = [
            sim_component["id"]
            for sim_component in sim_components
            if sim_component.get("containerID", "") == container["id"]
        ]
        for container_component_type_id in container.get("componentTypeIDs", []):
            if (
                container_component_type_id
                in sim_component_ids_with_matching_container_id
            ):
                continue
            if container_component_type_id not in component_types_ids:
                log.warning(
                    "Container %r contains a component type that is not defined. This is probably a bug.",
                    container["name"],
                )
                continue

            component_from_component_types = next(
                component_type
                for component_type in component_types
                if component_type.get("id") == container_component_type_id
            )
            dummy_id = component_from_component_types.get("id", "")
            dummy_name = component_from_component_types.get("name", "")

            dummy_component = Component(
                is_dummy=True,
                uuid="",
                id=dummy_id,
                name=dummy_name,
                type="",
                item_class=[],
                is_enabled=False,
                is_main=False,
                input_variables={},
                components={},
                parameters={},
            )
            dummy_components[dummy_name] = dummy_component

    return dummy_components


def _get_all_subcomponent_uuids(components: list[dict[str, Any]]) -> set[str]:
    all_subcomponent_uuids = set()

    for component in components:
        for subcomponent in component.get("subcomponents", []):
            all_subcomponent_uuids.add(subcomponent["uuid"])

    return all_subcomponent_uuids


def _extract_input_variable(
    path: list[str], data: dict[str, Any], input_sources_mapping: dict[str, InputSource]
) -> InputVariable:
    input_variable_path = path + [data["id"]]

    input_variable = InputVariable(
        id=data["id"],
        uuid=data["uuid"],
        path=input_variable_path,
        display_name=data["display"],
        source=_extract_input_variable_source(data, input_sources_mapping),
        scale=data["scaling"],
        offset=data["offset"],
    )
    return input_variable


def _extract_input_variable_source(
    input_variable: dict[str, Any], input_sources_mapping: dict[str, InputSource]
):
    data_source_type = input_variable["dataSourceType"]
    if data_source_type == "static":
        return InputVariableStaticSource(value=input_variable["value"])
    elif data_source_type in ["scenario", "control_machines"]:
        data_source_id = input_variable["dataSourceID"]
        tag_source = input_variable["tagSource"]
        input_source = input_sources_mapping[data_source_id]
        if (
            tag_source["projectID"] != input_source.project_id
            or tag_source["scenarioID"] != input_source.scenario_id
        ):
            raise ValueError("Tag source does not match selected input source")
        return InputVariableScenarioSource(input_source, tag=tag_source["tag"])
    else:
        raise ValueError(f"Invalid data source type: {data_source_type}")


def _extract_input_variables(
    path: list[str],
    component: dict[str, Any],
    input_sources_mapping: dict[str, InputSource],
) -> dict[str, InputVariable]:
    variables = component.get("inputVariables", [])
    variables_list: list[InputVariable] = [
        _extract_input_variable(path, variable, input_sources_mapping)
        for variable in variables
    ]
    return {variable.id: variable for variable in variables_list}

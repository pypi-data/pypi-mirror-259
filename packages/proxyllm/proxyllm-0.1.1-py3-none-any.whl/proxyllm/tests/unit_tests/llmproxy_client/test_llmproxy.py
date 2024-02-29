import os

import pytest
import yaml
from llmproxy.utils.exceptions.provider import UnsupportedModel

from proxyllm.config.internal_config import internal_config
from proxyllm.llmproxy import (
    LLMProxy,
    UserConfigError,
    _setup_available_models,
    _setup_user_models,
)

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PATH_TO_ENV_TEST = ".env.test"


def test_empty_model() -> None:
    # This need to be the specific exception that it would raise
    # You need to merge main for the updated exceptions
    with pytest.raises(Exception, match="No models provided in llmproxy.config.yml"):
        LLMProxy(
            path_to_user_configuration=f"{CURRENT_DIRECTORY}/empty_model_test.yml",
            path_to_env_vars=".env.test",
            route_type="cost",
        )


def test_no_user_setting(tmp_path) -> None:
    yml_content = """
    """
    yml_path = tmp_path / "test_settings.yml"
    with open(yml_path, "w", encoding="utf-8") as file:
        file.write(yml_content)
    text = "Configuration not found, please ensure that you the correct path and format of configuration file"
    with pytest.raises(UserConfigError, match=text):
        LLMProxy(
            path_to_user_configuration=yml_path,
            path_to_env_vars=PATH_TO_ENV_TEST,
            route_type="category",
        )


def test_no_model_in_user_setting(tmp_path) -> None:
    yml_content = """
    provider_settings:
    """
    yml_path = tmp_path / "test_settings.yml"
    with open(yml_path, "w", encoding="utf-8") as file:
        file.write(yml_content)
    text = "No models found in user settings. Please ensure the format of the configuration file is correct."
    with pytest.raises(UserConfigError, match=text):
        LLMProxy(
            path_to_user_configuration=yml_path,
            path_to_env_vars=PATH_TO_ENV_TEST,
            route_type="category",
        )


def test_invalid_model() -> None:
    with pytest.raises(UnsupportedModel):
        LLMProxy(
            path_to_user_configuration=f"{CURRENT_DIRECTORY}/invalid_model_test.yml",
            path_to_env_vars=".env.test",
        )


def test_get_settings_from_yml(tmp_path) -> None:
    yml_content = """
    provider_settings:
      - provider: OpenAI
        api_key_var: OPENAI_API_KEY
        max_output_tokens: 256
        temperature: 0.1
        models:
            - gpt-3.5-turbo-instruct
            - gpt-3.5-turbo-1106
            - gpt-4
            - gpt-4-32k
    """
    yml_path = tmp_path / "test_settings.yml"
    with open(yml_path, "w", encoding="utf-8") as file:
        file.write(yml_content)

    LLMProxy(
        path_to_user_configuration=yml_path,
        path_to_env_vars=PATH_TO_ENV_TEST,
        route_type="category",
    )


def test_get_settings_from_invalid_yml() -> None:
    invalid_yml_path = "invalid_settings.yml"
    with pytest.raises((FileNotFoundError, yaml.YAMLError)):
        LLMProxy(
            path_to_user_configuration=invalid_yml_path,
            path_to_env_vars=PATH_TO_ENV_TEST,
        )


def test_setup_available_models() -> None:
    _setup_available_models(settings=internal_config)


def test_setup_user_models() -> None:
    path_to_user_configuration_test = f"{CURRENT_DIRECTORY}/test.yml"
    LLMProxy(
        path_to_user_configuration=path_to_user_configuration_test,
        path_to_env_vars=PATH_TO_ENV_TEST,
        route_type="cost",
    )


def test_no_available_model_UserConfigError() -> None:
    text = "Available models not found, please ensure you have the latest version of LLM Proxy."
    with pytest.raises(
        UserConfigError,
        match=text,
    ):
        _setup_user_models(available_models={}, yml_settings={})


def test_setup_user_models_no_setting_UserConfigError():
    with pytest.raises(
        UserConfigError,
        match="Configuration not found, please ensure that you the correct path and format of configuration file",
    ):
        test_available_model = _setup_available_models(settings=internal_config)
        _setup_user_models(available_models=test_available_model, yml_settings={})


def test_setup_user_models_empty_user_settings():
    with pytest.raises(
        UserConfigError,
        match="No models found in user settings. Please ensure the format of the configuration file is correct.",
    ):
        test_available_model = _setup_available_models(settings=internal_config)
        _setup_user_models(
            available_models=test_available_model,
            yml_settings={"provider_settings": []},
        )


def test_setup_user_models_no_variation() -> None:
    with pytest.raises(
        UserConfigError,
    ):
        test_available_model = _setup_available_models(settings=internal_config)

        _setup_user_models(
            available_models=test_available_model,
            yml_settings={
                "provider_settings": [
                    {
                        "provider": "OpenAI",
                        "api_key_var": "OPENAI_API_KEY",
                        "max_output_tokens": 256,
                        "temperature": 0.1,
                        "models": None,
                    }
                ]
            },
        )


def test_invalid_route_type_constructor() -> None:
    prompt = "what's 9+10?"
    with pytest.raises(UserConfigError):
        test = LLMProxy(
            route_type="bad_route_type",
            path_to_user_configuration=f"{CURRENT_DIRECTORY}/test.yml",
            path_to_env_vars=".env.test",
        )
        test.route(prompt=prompt)


def test_llmproxy_invalid_route_type_in_yaml_config(tmp_path):
    yml_content = """
    proxy_configuration:
      route_type: asdfasdfasd

    provider_settings:
      - provider: OpenAI
        api_key_var: OPENAI_API_KEY
        max_output_tokens: 256
        temperature: 0.1
        models:
            - gpt-3.5-turbo-instruct
            - gpt-3.5-turbo-1106
            - gpt-4
            - gpt-4-32k
    """
    yml_path = tmp_path / "test_settings.yml"
    with open(yml_path, "w", encoding="utf-8") as file:
        file.write(yml_content)

    with pytest.raises(UserConfigError):
        proxy = LLMProxy(
            path_to_user_configuration=yml_path,
            path_to_env_vars=PATH_TO_ENV_TEST,
        )
        proxy.route(prompt="What is 1 + 1")


def test_llmproxy_constructor_route_type_override(tmp_path):
    yml_content = """
    proxy_configuration:
      route_type: cost 

    provider_settings:
      - provider: OpenAI
        api_key_var: OPENAI_API_KEY
        max_output_tokens: 256
        temperature: 0.1
        models:
            - gpt-3.5-turbo-instruct
            - gpt-3.5-turbo-1106
            - gpt-4
            - gpt-4-32k
    """
    yml_path = tmp_path / "test_settings.yml"
    with open(yml_path, "w", encoding="utf-8") as file:
        file.write(yml_content)

    proxy = LLMProxy(
        path_to_user_configuration=yml_path,
        path_to_env_vars=PATH_TO_ENV_TEST,
        route_type="category",
    )

    assert proxy.route_type == "category"

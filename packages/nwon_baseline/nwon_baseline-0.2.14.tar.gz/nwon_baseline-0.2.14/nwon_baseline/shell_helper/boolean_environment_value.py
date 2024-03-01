from os import getenv


def boolean_environment_value(name: str, default_value: bool | None = None) -> bool:
    """
    Parses an environment variable to boolean
    """

    true_ = (
        "true",
        "1",
        "t",
        "yes",
        "on",
    )  # Add more entries if you want, like: `y`, `yes`, `on`, ...

    false_ = (
        "false",
        "0",
        "f",
        "no",
        "off",
    )  # Add more entries if you want, like: `n`, `no`, `off`, ...

    value = getenv(name)

    if value is None:
        if default_value is None:
            raise ValueError(f"Environment variable `{name}` not set!")

        return default_value

    if value.lower() not in true_ + false_:
        return False

    return value.lower() in true_

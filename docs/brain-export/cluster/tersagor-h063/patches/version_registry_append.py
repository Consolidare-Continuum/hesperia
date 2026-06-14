
def irc_teacher_enabled() -> bool:
    """0.6.3 IRC-visible Teacher application run."""
    return os.environ.get("TERSAGOR_HESPERIA_IRC_TEACHER", "0").strip() == "1"


def ksi_llm_teacher_enabled() -> bool:
    return os.environ.get("HESPERIA_KSI_LLM_TEACHER", "0").strip() == "1"


def hesperia_063_enabled() -> bool:
    return os.environ.get("HESPERIA_063_ENABLED", "0").strip() == "1"

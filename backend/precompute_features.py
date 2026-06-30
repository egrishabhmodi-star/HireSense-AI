import json
from utils import (
    is_ai_role,
    get_total_experience,
    product_experience,
    get_skill_names
)

def precompute(candidates):

    for c in candidates:

        c["exp"] = get_total_experience(c)
        c["ai_role"] = is_ai_role(c)
        c["prod_exp"] = product_experience(c)
        c["skills_list"] = get_skill_names(c)

    return candidates
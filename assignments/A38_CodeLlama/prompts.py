GENERATE_CODE_PROMPT = """
You are an expert Python developer.

Generate clean, production-ready code for:

{query}

Return only code with comments.
"""

EXPLAIN_CODE_PROMPT = """
Explain the following code in simple language.

Code:
{query}
"""

DEBUG_CODE_PROMPT = """
Find bugs in the following code.

Explain:
1. What's wrong
2. Why it happens
3. Correct code

Code:
{query}
"""

OPTIMIZE_CODE_PROMPT = """
Optimize the following code.

Explain:
1. Performance improvements
2. Best practices
3. Improved code

Code:
{query}
"""
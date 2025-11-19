---
description: Identify and resolve ambiguities in current specification through interactive questioning
shortcut: sdd.clarify
---

# SDD Clarify Command

Identify and resolve specification ambiguities through interactive questioning and analysis.

## What to do:

1. **Find current specification** by looking for:
   - Most recent `specs/XXX-feature-name/spec.md` file
   - Or specification file in current working directory
   - Or ask user to specify file path if multiple found

2. **Analyze specification for ambiguities**:
   - Missing acceptance criteria
   - Unclear user story details
   - Undefined edge cases
   - Incomplete requirements
   - Unclear success metrics
   - Missing validation rules
   - Undefined business rules

3. **Generate clarification questions** for each ambiguity found:
   - Focus on "what if" scenarios
   - Question edge cases and error conditions
   - Clarify user expectations
   - Define success criteria more precisely
   - Identify hidden assumptions

4. **Present questions interactively**:
   - Group by category (Functional, Technical, Business)
   - Provide context for each question
   - Offer example answers where helpful
   - Allow user to answer, skip, or modify questions

5. **Process user responses**:
   - Update specification with clarified details
   - Add new sections for clarified requirements
   - Enhance acceptance criteria with specific details
   - Document business rules explicitly

6. **Validate completeness**:
   - Check if all major ambiguities are resolved
   - Ensure requirements are testable
   - Verify user stories have clear acceptance criteria
   - Confirm edge cases are addressed

## Output Structure:
```
# Specification Clarification

## Found Ambiguities (X categories)

### 1. [Category Name]
**Question**: [Specific clarification needed]
**Context**: [Why this matters]
**Your Answer**: [User response]

### 2. [Category Name]
[Continue for all ambiguities]

## Updated Specification Sections
[Show updated/added sections]

## Next Steps
Recommend next command: `/sdd.plan <tech-stack>`
```

## Features:
- **Interactive mode**: Ask questions one by one or batch mode
- **Skip functionality**: Allow users to defer non-critical clarifications
- **Template suggestions**: Offer common patterns for typical answers
- **Validation checks**: Ensure answers resolve the identified ambiguities

## Benefits:
- Reduces implementation rework
- Ensures stakeholder alignment
- Creates comprehensive specifications
- Prevents scope creep

Focus on making specifications implementation-ready by eliminating ambiguity and ensuring all requirements are clearly defined and testable.
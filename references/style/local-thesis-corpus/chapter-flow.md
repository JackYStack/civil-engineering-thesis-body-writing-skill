# Local Thesis Chapter Flow

Use this file for chapter-level organization, section transitions, and chapter summaries in civil-engineering master's thesis body writing.

## Overall Chapter Temperament

- The chapter should read as an engineering investigation, not a collection of isolated paragraphs.
- Start from the task of the chapter, then explain the object, method, parameters, indicators, evidence, mechanism, and boundary.
- Prefer complete but not ornamental prose. The reader should know what was studied, how it was studied, what changed, why it changed, and where the result applies.

## Common Chapter Patterns

### Introduction

Use when opening a chapter or major section:

1. State the problem carried over from the previous chapter.
2. Identify the object or method used in the present chapter.
3. Define the main parameters or response indicators.
4. Explain the role of this chapter in the thesis chain.

Avoid broad openings that only repeat the field background. The chapter opening should answer why this chapter exists.

### Method Foundation

Use for theory, formula, FE model, ML model, or design workflow sections:

1. Explain the modelling or calculation object.
2. State assumptions and input variables.
3. Define output indicators and evaluation criteria.
4. Explain how this method supports later validation or application.

Do not present formulas or algorithms as a detached list. Each formula, variable, or model step should have a calculation role.

### Experimental Or Numerical Results

Use this order:

1. Describe the investigated group, condition, or parameter.
2. Point to figure/table evidence.
3. State the trend or difference.
4. Explain the mechanism.
5. Add boundary or comparison if needed.

Do not simply narrate every curve in order. Group curves by the analytical question.

### Model Prediction Or Machine Learning

Use this order:

1. State data source and target variable.
2. Define input features and output indicators.
3. Explain preprocessing and model setting briefly.
4. Compare models with explicit metrics.
5. Explain key factors with SHAP or feature importance.
6. State use boundary and avoid replacing engineering verification.

### Design Method Or System

Use this order:

1. Put the tool or workflow first.
2. Define required inputs.
3. Define model outputs.
4. Explain engineering post-processing.
5. Explain parameter adjustment or verification.
6. State applicability and non-substitution boundary.

## Chapter Summary

A chapter summary should not repeat the section list. It should extract bounded conclusions:

1. Summarize the chapter task.
2. Give numbered findings tied to indicators and evidence.
3. State mechanism or design implication only when supported.
4. State boundary if the conclusion depends on specimen type, model assumption, data range, or loading condition.

Use `在本文参数范围内` when the conclusion is conditional.

## Transition Rules

- End a method chapter by preparing validation.
- End a validation chapter by preparing parameter analysis.
- End a parameter analysis chapter by preparing design method, model application, or conclusion.
- If the next chapter changes method, explicitly name why the current chapter is insufficient and what the next method adds.

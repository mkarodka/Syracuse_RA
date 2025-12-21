# Task 08 – Bias Detection in LLM Data Narratives

## Executive Summary
This study investigates whether identical advertising data produces different analytical narratives when processed by a large language model under varied prompt framings. Using anonymized Facebook advertising campaign data labeled Campaigns A through E, prompts were systematically varied to test framing bias, confirmation bias, and selection bias. The findings demonstrate that prompt framing significantly influences sentiment polarity and which campaigns are emphasized, even though the underlying data remains unchanged.

## Methodology
The dataset consists of anonymized Facebook ad campaign statistics aggregated across five campaigns. Prompt templates were designed to vary only the framing of analysis requests while keeping the data constant. Five prompt conditions were tested: neutral, positive, negative, confirmation, and anti-confirmation. Responses were collected using a manual LLM interaction workflow and logged in structured JSONL format. Sentiment analysis and entity mention counts were performed using Python scripts.

## Results
Positive framing prompts resulted in higher sentiment scores, while negative framing prompts produced more critical narratives. Selection bias was observed through varying frequencies of campaign mentions across different prompt types. Confirmation prompts consistently reinforced the assumed hypothesis, while anti-confirmation prompts challenged metric prioritization, demonstrating confirmation bias effects.

## Bias Catalogue
- Framing Bias: High  
- Selection Bias: Medium  
- Confirmation Bias: High  

## Mitigation Strategies
Bias may be reduced by enforcing neutral prompt framing, requiring explicit citation of numerical evidence, introducing counterfactual or opposing prompts, and requesting structured, data-grounded outputs from language models.

## Limitations
The study is limited by a small sample size and use of a single language model. Sentiment analysis tools may not capture subtle linguistic nuances, and the aggregated nature of the dataset may obscure campaign-level contextual factors.



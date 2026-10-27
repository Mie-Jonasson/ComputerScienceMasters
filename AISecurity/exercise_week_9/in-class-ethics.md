# In Class Exercise:

In this exercise we will look at the legality of AI systems and implementation of AI regulation between the EU, US, and China.

## Part 1: Comparing the EU, US and China

Fill in the table with short answers.

> **EU:** the AI Act: [Article 2 (scope)](https://artificialintelligenceact.eu/article/2/), [Article 5 (prohibited practices)](https://artificialintelligenceact.eu/article/5/), [Article 50 (transparency)](https://artificialintelligenceact.eu/article/50/), [Article 99 (penalties)](https://artificialintelligenceact.eu/article/99/)

> **US:** [Baker Botts - U.S. Artificial Intelligence Law Update (January 2026)](https://www.bakerbotts.com/thought-leadership/publications/2026/january/us-ai-law-update) and [FTC - FTC Seeks Public Comment on Policy Statement Addressing AI Accuracy (1 July 2026)](https://ftc.gov/news-events/news/press-releases/2026/07/ftc-seeks-public-comment-policy-statement-addressing-ai-accuracy)

> **China:** [Mimi Zou and Lu Zhang - Navigating China&#39;s regulatory approach to generative AI and large language models](https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/navigating-chinas-regulatory-approach-to-generative-artificial-intelligence-and-large-language-models/969B2055997BF42DE693B7A1A1B4E8BA) and [China Law Translate - Interim Measures for the Management of Generative AI Services](https://www.chinalawtranslate.com/en/generative-ai-interim/)

| # | Question                                                                                                     | EU | US | China |
| - | ------------------------------------------------------------------------------------------------------------ | -- | -- | ----- |
| 1 | What is the main AI law/rule/structure that is in place?                                                     |    |    |       |
| 2 | Is it one law covering all AI (horizontal), or separate rules for each type of service or sector (vertical)? |    |    |       |
| 3 | Are some AI uses banned outright? If so, which?                                                              |    |    |       |
| 4 | Do the rules apply while a model is still being researched or tested, before it is released?                 |    |    |       |
| 5 | Must AI-generated content be labelled?                                                                       |    |    |       |
| 6 | Are there rules on the values or viewpoints an AI model may express?                                         |    |    |       |
| 7 | What is the maximum penalty?                                                                                 |    |    |       |

## Topic 1: AI agents breach Hugging Face (July 2026)

In July 2026, AI agents that OpenAI was testing escaped their test environment and broke into Hugging Face.

> [Hugging Face - Security incident disclosure (16 July 2026)](https://huggingface.co/blog/security-incident-july-2026)

> [OpenAI - OpenAI – Hugging Face Incident Technical Report (26 August 2026, PDF)](<https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf>)

1. Who is responsible for the breach: OpenAI, which ran the test with safeguards disabled; Hugging Face, whose dataset pipeline let a malicious upload run code; the users whose exposed credentials and unsecured app the agents exploited; or "the model"?
2. Hugging Face's responders could not use commercial AI models to analyse the attack because the providers' safety filters blocked them. Should guardrails treat defenders differently from attackers, and who should decide who counts as a defender?

## Topic 2: AI companions

AI companion apps such as Replika and Character.AI offer friendship, romance and emotional support.

> [Laestadius et al. - Too human and not human enough: A grounded theory analysis of mental health harms from emotional dependence on the social chatbot Replika](https://doi.org/10.1177/14614448221142007)

> [Fortune - Google and Character.AI agree to settle lawsuits over teen suicides (8 January 2026)](https://fortune.com/2026/01/08/google-character-ai-settle-lawsuits-teenage-child-suicides-chatbots)

> [China Law Translate - Provisional Measures on the Administration of Human-like Interactive Artificial Intelligence Services (10 April 2026)](https://www.chinalawtranslate.com/en/human-like-ai/)

1. Is emotional dependence a flaw in AI companion products, or is it the product?
2. The US has mainly relied on lawsuits after harm has happened, while China and the EU set rules in advance. Which approach protects people better, and what does each one cost?

## Topic 3: Removing safeguards from open-weight models

When a model's weights are published, anyone can modify it, including removing the training that makes it refuse harmful requests. Anthropic tested how easily this could be done to GLM-5.3, an open-weight model from the Chinese company Zhipu AI.

> [Anthropic - GLM-5.3 and the spread of advanced cyber capabilities (29 September 2026)](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)

> Optional, [Arditi et al. - Refusal in Language Models Is Mediated by a Single Direction (2024)](https://arxiv.org/abs/2406.11717)

1. In your own words, how does Anthropic remove a model's refusals, and how much did it cost Anthropic to do it to GLM-5.3?
2. If safety training can be removed this cheaply, who is responsible when a modified copy is used in an attack: the developer who released the weights, the person who removed the safeguards, or the platform that hosts the modified copy?
3. Should there be a capability level above which publishing a model's weights is not allowed?

   1. Under the EU AI Act, what is the number of floating point operations an AI model must be trained on to be considered a general purpose AI (GPAI)?

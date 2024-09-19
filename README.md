## Introduction

Welcome to RhymeLearn, an innovative application that transforms the traditional way of
learning by converting textbook content into rap lyrics. This guide will walk you through the
process of using RhymeLearn to make educational material more engaging and memorable.

Motivation: Hamilton (Musical)

## Usage

1. Go to the provided URL where RhymeLearn is hosted.

2. In the textbox, paste the textbook content you want to transform.

3. Choose an Artist

4. Click the "Submit" button to start the transformation process.

### Example Inputs/Outputs

#### Example 1: Laplace Smoothing(Speech and Language Processing)
- Input: "The simplest way to do smoothing is to add one to all the n-gram counts, before we normalize them into
probabilities. All the counts that used to be zero will now have a count of 1, the counts of 1 will be 2, and so on.
This algorithm is called Laplace smoothing. Laplace smoothing does not perform well enough to be used in modern
n-gram models, but it usefully introduces many of the concepts that we see in other smoothing algorithms, gives a
useful baseline, and is also a practical smoothing algorithm for other tasks like text classification.”
- Artist: Eminem
- Output: (Rap lyrics)
"Yo, check it, the rhyme's raw, statistics on the track
N-gram counts, probabilities, ain't no turning back
Smoothing out the data, making it less wack
Laplace stepping in, putting zeros on the attack
…”
#### Example 2: Industrial Revolution(Wikipedia)
- Input: "The Industrial Revolution, sometimes divided into the First Industrial Revolution and Second Industrial
Revolution, was a period of global transition of the human economy towards more widespread, efficient and stable
manufacturing processes that succeeded the Agricultural Revolution. Beginning in Great Britain, the Industrial
Revolution spread to continental Europe and the United States, during the period from around 1760 to about
1820–1840. This transition included going from hand production methods to machines; new chemical
manufacturing and iron production processes; the increasing use of water power and steam power; the development
of machine tools; and the rise of the mechanized factory system. Output greatly increased, and the result was an
unprecedented rise in population and the rate of population growth. The textile industry was the first to use modern
production methods, and textiles became the dominant industry in terms of employment, value of output, and
capital invested.”
- Artist: Snoop Dogg

- Output: (Rap lyrics)
"Yo, check it, it's the D-O-double G, back with a history lesson
Bout the Industrial Revolution, where things got stressin'
Started in Great Britain, yeah, they was the first
To ditch the hand tools, puttin' machines to work, that's what's up
From farms to factories, the world transformed
Steam power and iron, a new era was born
…”

## Documentation
### Models: Gemini 1.5 Pro
Architecture: Transformer and Mixture-of-Experts (MoE) architecture
Training: Gemini 1.5 Pro is trained on multiple 4096-chip pods of Google’s TPUv4 accelerators,
distributed across multiple datacenters, and on a variety of multimodal and multilingual data.
The pre-training dataset includes data sourced across many dierent domains, including web
documents and code, and incorporates image, audio, and video content. For the instruction-
tuning phase they finetuned Gemini 1.5 Pro on a collection of multimodal data (containing
paired instructions and appropriate responses), with further tuning based on human preference
data.
Known Limitations: Gemini models can exhibit limitations outlined in the prior Gemini 1.0
Technical Report (Gemini-Team et al., 2023)
### Datasets
The Rap Lyrics dataset consists of text files(github) that were scraped from the Genius API and
subsequently converted into a CSV format.
Size: 186630 rows, each row consists of artist name and lyrics
### Frameworks
1. vertexai:
GenerativeModel: represents a machine learning model capable of generating content.
generation_config: Configuration parameters for the content generation process, like output
token limit and creativity settings (temperature and top_p).
safety_settings: Provides configurations to prevent the model from generating harmful content by
specifying thresholds for blocking different categories of harmful speech.
2. gtts (Google Text-to-Speech): A Python library and tool that interfaces with Google's Text-to-
Speech API. It converts the generated lyrics into spoken words, outputting an audio file.
3. gradio

### Experiments:
My experiments aimed to explore the capabilities of language models—Gemini 1.5, GPT-3.5,
and a fine-tuned GPT-2—in transforming complex textbook content into rap lyrics. 


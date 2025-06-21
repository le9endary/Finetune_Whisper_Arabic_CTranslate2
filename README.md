# Finetuning Whisper for Arabic Transcription Converting to CTranslate2 for Fast Inference

## Project Overview
The project was to fine-tune automatic speech recognition (ASR) model, specifically targeting the Arabic Omani dialect. The objective was to enhance Whisper model performance for Omantel's customer service calls by ensuring highly accurate localized speech transcription through customized fine-tuning and fast inference on large call data. The end goal was to get AI analytics from  customer calls.

## Dataset
For Fine-tuning I have used Omantel customer service data of Omani accent. I have also added open source data from Arabic speech org to increase the dataset. Other open source dataset can be used is Mozilla's Common Voice, which is used in this repo guide as our data was confidential.

## Whisper Model and Fine-tuning
Whisper is an ASR model for multilingual support. Fine-tuning specifically targeted Arabic language patterns, focusing on nuances and phonetics unique to the Omani dialect, improving localized transcription accuracy.


## Precision Formats
FP16 was used to speed up computations during both training and inference. Using FP16 reduced memory requirements and computation times, beneficial for training and deploying deep learning models in resource-constrained environments. INT8 quantization also can be used to optimize the model by significantly decreasing memory usage and computational needs.

## CTranslate2
CTranslate2 is a library for efficient inference with Transformer models. It applies many performance optimization techniques such as weights quantization, layers fusion and batch reordering to accelerate and reduce the memory usage of Transformer models.
After fine-tuning we converted our model to CTranslate2 for fast inference using faster whisper library.


## Training Configuration and Evaluation
The training utilized HuggingFace Transformers and Accelerate libraries for robust natural language processing capabilities. Evaluation was performed using Word Error Rate (WER) a standard metric in speech recognition tasks. Training parameters included gradient accumulation, gradient checkpointing, and mixed precision computing (FP16)

## HuggingFace Hub
The fine-tuned Whisper model was uploaded to the HuggingFace Hub for facilitating easy initial testing, sharing, and collaboration.

## Furthur Results improvment 
After fine tuning we observed better results and WER, however to further increase accuracy we used LLM layer as last step. The LLM was given prompt to correct grammer or words in Arabic dialect for better transcription. Since, the end goal was to do AI analytics on the transcription thats why correcting words using LLM layers was important.


## Conclusion
Through fine-tuning, precision optimization, and using CTranslate2, the Whisper model was effectively tailored to transcribe Arabic speech accurately for the Omani dialect. The final optimized model was hosted on AWS EC2 instance to empowers Omantel’s customer service with enhanced localized speech transcription capabilities and AI analytics.














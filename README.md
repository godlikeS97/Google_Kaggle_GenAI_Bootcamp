# Google_Kaggle_GenAI_Bootcamp

## Capstone Project: AI Art Gallery Tour Guide

### Project Overview
An intelligent art gallery tour guide system that leverages Large Language Models (LLMs) and computer vision capabilities to generate detailed, contextual explanations for artworks. The system combines structured metadata with visual analysis using the Metropolitan Museum of Art's collection data.

### Key Features
1. **Data Processing & Preparation**
   - Processed Met Museum dataset (50 sample artworks from Drawings and Prints)
   - Optimized feature selection (35 columns)
   - Maintained image URLs for visual analysis

2. **Baseline Implementation**
   - Prompt engineering framework using Gemini API
   - Structured prompts with artwork metadata
   - Comprehensive evaluation system with quality ratings

3. **Generation Control & Optimization**
   - Token length control (200 tokens)
   - Response length analysis and quality correlation
   - Generation quality evaluation across constraints

4. **Multimodal Integration**
   - Image processing with Gemini's multimodal capabilities
   - Combined textual and visual analysis
   - Image-aware evaluation framework

### Technical Stack
- Python 3.x
- Key Libraries:
  - python-dotenv (environment variables)
  - pandas (data processing)
  - google-generativeai (Gemini API)
  - requests (HTTP requests)
  - tqdm (progress tracking)
  - aiohttp (async HTTP)

### Project Structure
```
/Capstone Project
├── data/
│   ├── met_with_images.csv
│   └── sample50_df_drawings_and_prints.csv
├── demo.ipynb
├── results/
│   ├── baseline/
│   ├── output_length_control/
│   └── image_input/
└── README.md
```

For detailed setup and usage instructions, refer to the project's dedicated README in the Capstone Project directory.

## Course Content

### Day 1: Prompting and Evaluation
- **Prompting Fundamentals**: 
  - Introduction to prompt engineering
  - Best practices for working with LLMs
  - Techniques for effective prompt design
- **Evaluation and Structured Output**: 
  - Techniques for evaluating LLM outputs
  - Automated evaluation methods
  - Pointwise and pairwise evaluation approaches
  - Working with structured outputs
  - Practical evaluation challenges and solutions
- **Reference Materials**:
  - Foundational Large Language Models & Text Generation
  - Prompt Engineering Best Practices
  - NeurIPS Evaluation Guidelines

### Day 2: Embeddings, Classification and RAG
- **Embeddings and Similarity**: 
  - Working with embeddings from Gemini API
  - Calculating and utilizing similarity scores
  - Understanding vector representations
- **Classification with Keras**: 
  - Using embeddings for classification tasks
  - Implementing neural networks with Keras
  - Building classification models
- **Document Q&A with RAG**: 
  - Implementation of Retrieval-Augmented Generation (RAG)
  - Using Chroma for document storage and retrieval
  - Building Q&A systems with RAG architecture
- **Reference Materials**:
  - Embeddings and Vector Stores Guide
  - Task-Aware Embedding Implementation

### Day 3: Function Calling and Agent Building
- **Function Calling with Gemini API**: 
  - Understanding function calling capabilities
  - Building chat interfaces with automatic function calling
  - Practical implementation of function-enabled conversations
- **Building Agents with LangGraph**: 
  - Introduction to LangGraph framework
  - Creating and deploying AI agents
  - Implementing agent-based workflows and interactions
- **Reference Materials**:
  - AI Agents Implementation Guide
  - Agents Companion Guide

### Day 4: Model Fine-tuning and Search Integration
- **Fine-tuning Custom Models**: 
  - Understanding model fine-tuning concepts
  - Implementing task-specific model customization
  - Best practices for fine-tuning Gemini models
- **Google Search Integration**: 
  - Incorporating Google Search results with Gemini API
  - Implementing search-based grounding
  - Building real-time information retrieval systems
- **Reference Materials**:
  - Solving Domain-Specific Problems using LLMs

### Day 5: Course Completion
*No practical sessions. Please review the materials from previous days and complete any pending exercises.*
- **Reference Materials**:
  - Operationalizing Generative AI on Vertex AI
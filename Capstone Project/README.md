# AI Art Gallery Tour Guide

## Project Description
This project implements an intelligent art gallery tour guide system using Large Language Models (LLMs) and computer vision capabilities. The system generates detailed, contextual explanations for artworks by combining structured metadata with visual analysis, using the Metropolitan Museum of Art's collection data.

### Key Components

1. **Data Processing & Preparation**
   - Processed Met Museum dataset with 50 sample artworks from Drawings and Prints department
   - Cleaned and filtered features, reducing from 55 to 35 columns by removing those with >70% null values
   - Excluded URL and ID columns for cleaner prompt generation
   - Maintained image URLs for visual analysis integration

2. **Baseline Implementation**
   - Developed prompt engineering framework using Gemini API
   - Created structured prompts incorporating artwork metadata (artist info, historical context, physical details)
   - Implemented comprehensive evaluation system with quality ratings
   - Generated and evaluated explanations with rate limiting (15 calls per minute)

3. **Generation Control & Optimization**
   - Implemented token length control (200 tokens) for concise explanations
   - Analyzed correlation between response length and quality ratings
   - Evaluated generation quality across different length constraints
   - Analyzed poor-quality generations to identify improvement areas

4. **Multimodal Integration**
   - Enhanced system with image processing using Gemini's multimodal capabilities
   - Combined textual metadata with visual analysis for richer artwork descriptions
   - Developed specialized prompt template balancing textual and visual information
   - Implemented image-aware evaluation framework

### Technical Implementation
- Used Google's Gemini API (gemini-2.0-flash model) for:
  - Text generation
  - Image analysis
  - Response evaluation
- Implemented systematic rate limiting:
  - 15 calls/minute for generation
  - 8 calls/minute for evaluation
- Built data processing pipelines for artwork metadata
- Created automated evaluation workflows with progress tracking

### Data Management
- Structured data storage in CSV format:
  - Baseline generations and evaluations
  - Length-controlled generations and evaluations
  - Image-enhanced generations and evaluations
- Implemented progressive saving for long-running evaluations

## Project Structure
```
/Capstone Project
├── data/
│   ├── met_with_images.csv           # Original dataset
│   └── sample50_df_drawings_and_prints.csv  # Sampled dataset
├── demo.ipynb                        # Main implementation notebook
├── results/
│   ├── baseline/                     # Baseline generation results
│   ├── output_length_control/        # Length-controlled results
│   └── image_input/                  # Image-enhanced results
└── README.md                         # Project documentation
```

## Technical Requirements
- Python 3.x
- Required packages:
  - python-dotenv (environment variables)
  - pandas (data processing)
  - google-generativeai (Gemini API)
  - requests (HTTP requests)
  - tqdm (progress tracking)
  - aiohttp (async HTTP)

## Setup
1. Install required packages:
```bash
pip install python-dotenv pandas google-generativeai requests tqdm aiohttp
```
2. Configure environment variables:
   - Create `.env` file with Gemini API key
3. Prepare data:
   - Download Met Museum dataset
   - Run data preprocessing steps in demo.ipynb

## Usage
The system processes artwork metadata and images to generate detailed, contextual explanations suitable for gallery visitors. Each generation undergoes quality evaluation and is stored with structured ratings for analysis.
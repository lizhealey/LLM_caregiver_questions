# LLM_caregiver_questions


## Code to reproduce study

## Code/
1_submit_batch.ipynb --> generates prompts, submits API batch, and saves subset for chat interface eval

2_LLM_judge.ipynb --> runs LLM judge using LLM_judge.py

3_analyze.ipynb --> Generates Figure 1

4_human_eval/ --> random subset generation code, GUI for human eval 

5_kappa/ --> generates kappa result 

6_example.ipynb --> randomly loads three examples 


## data/
Contains all data artifacts. 
### batches_download/
The batches download directly from Claude and OpenAI (only OpenAI saves input data storage). Claude allows for a single batch to contain two models. OpenAI requires a separate batch per model, and so there is one Claude file and two OpenAI files. 

### random_subset/
This contains the random subset of the no_context prompts that were tested on the web interface. It also contains the files with the ChatGPT and Claude output, entered manually. 

### raw_output/
This contains the output of the batch API (A post-processed version of the files in batches_download/)

### parsed_output/
This contains the results of the LLM judge. 

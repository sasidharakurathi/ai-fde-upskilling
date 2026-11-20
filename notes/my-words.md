# In My Own Words

For each lesson, answer the **Explain it back** questions here, **without looking** at the lesson.
Wrong answers are fine, because that's how learning starts. After Claude checks your answers, **don't delete
what you wrote**. Add a line starting with `Correction:` underneath instead, so you can see how you improved.

---

## Lesson 0.1 · AI vs ML vs DL vs GenAI vs LLM

### Try it (sorting)
1. Rules (not learning)
2. Rules (not learning) 
3. Machine Learning
4. Machine Learning
5. Deep Learning
6. Deep Learning
7. Generative AI (not an LLM)
8. LLM
9. Deep Learning

### Explain it back
1. Rules vs machine learning (my own example): okay bud, the old rule-based way is just a combination of certain set of conditions or rules, here we need to mention all the possbile or required combinations to make it work. The machine learning is a way where the model is trained on huge set of sample or example data such that the model pridicts the outcome of the new data based on the patterns of old data. For example: Let's consider a detecting an adult site, if we follow the old rule-based way then we need to write down all the keywords that comes in only in the adult sites which needs a huge list and also this list can change. But we can train a model with some set of existing data by labelling and categorizing them into "Adult site" or "Not an adult site", the model itself learns the patterns and predicts the new input sites as "Adult site" or "Not an adult site" with a condifence score.

2. Training / model / inference:
   1. Training: It is a process where the system learns the patterns based on the data given
   2. Model: After the training process the model is generated as an output. It a collection of billions of numbers which are the trained data and this model takes an input and generates an output.
   Correction: The model contains the learned patterns no the trained data.
   3. It is a process of givig input to AI or ML or DL models and generating an output.

3. What an LLM does at its core, and why "it looked it up" is usually wrong: the LLM takes an input text and tries to predict the next token based on it. Basically it generated the text. The "Claude looked it up online is wrong" because the LLM can only generate the text based on its trained data, it can not search in the internet by itself. To do that it needs a RAG or Search Tool.  

4. The circles, biggest to smallest, with my own example in each:
   1. AI is the biggest circle, the ML comes under the AI, the DL comes under the ML, the Generative AI comes under the DL and the LLM comes under the Generative AI.
   2. Any computer which does the tasks that basically needs a human like thinking comes under AI like predicting weather etc
   Correction: "predicting weather" not comes under AI its may come under ML. A system using something from the rules or search a way instead like: Goolge Maps fastest route etc.
   3. A computer which learns the patterns of huge data is called ML. The predicting weather can come under ML
   4. An ML with multiple layers of nueral networks called as DL. like embedding Images or search in images etc
   5. Anything which generates new content by itself comes under Generative AI, like creating new images, audios, videos etc
   6. A generative AI which can only generate text is called LLM. it can only predict and generate the text.
   Correction: many moderen LLMs can also take the images as input and generate the text as output.

---

## Lesson 0.2 · AI Engineer vs FDE

### Try it (AIE / FDE / BOTH)
1. AIE
2. FDE
3. AIE
4. FDE
5. FDE
6. BOTH
7. BOTH
8. FDE
9. AIE
10. FDE

Bonus: the 3 tasks that sounded most fun: 1,3,9 and 6 as well

### Explain it back
1. The difference, to a friend, in 3 sentences (my own analogy): Basically an AI Engineer is the person who works on building the AI based products using the LLMs or other Agents etc. An FDE work on commnuicating with the clients and integrating the products in the client's environments and carries the client's requriements or feedback to the AI Engineer team.

2. Three things both roles do: Both roles need to understand python and able to code in it. Both need to know the basics concepts like RAG etc. And both should be able to figure out why the app is slow.

3. Why an FDE must be honest about limits, and what goes wrong if not: It is important for the FDE because if a FDE gives wrong promises to the clients then it will cause any issue to the clients and the company aswell.
Correction: For example an FDE tell to an Finance Company that it always gives correct data. Then if it gives a wrong intrest rate to a customer then it will cause an issue. So the FDE should give the correct infromation like The product gives 95% correct data, it's recommended to do a human evaluation at the end.  

4. AI researcher vs ML Engineer vs AI Engineer: An AI researcher, does research on new things like training new models. ML Engineer train or retrain or run the custom ML models. AI Engineer uses exsitng models and builds the products using them like RAGs, Agents etc. 

---

## Lesson 0.3 · The parts of an AI app

### Try it
**Part A: trace "What's your return policy for shoes?"**
1. First the customer sends the question from the UI
2. The code checks who is the customer and what access he has, whether he is logged in or not and what data he has access to.
3. Then the relevant data of return plicy is retrieved from the Documents or database etc.
4. The the system prompt (aka instructions), context (fetched data) and the user question is combined to make it as a prompt
5. This prompt is sent to the LLM model. The model generates a output or response about on the instructions, data and question provided.
6. Then that response is sent through some guardrail checks to make sure no sensitve or harmful data is being provided.
7. And all this process inputs, outputs, data etc etc are logged and also measure the things like response time, answer quality etc.

**Part B: detective**
1. Data. The problem might be that the return policy data is not updated and the docs or database might still holds the old return ploicy (30 days) content.
2. Prompt and Guardrails. The problem most probably in the prompt itself, first I will check if the tone of the response is mentioned in the prompt or not. Also if the response contains the rude tone, first I will make sure the guardrails catches that and it is never sent to the customer or user.
3. Code. Here the problem can be in the backend code. The code might have accidently gave the other customers data access. So I would debug what access the code gave to the customer like is it his own data only or other customers data as well.  
4. Prompt and Code. Basically the models are stateless, they do not remember the old conversations once the response is given. So the code should attach the previous conversations as context to the prompt (api call).
5. Prompt. This could be two reasons the context (data) is very large or the instructions itself are large. Since you told 50 pages of instructions, I consider the problem is in the instructions and check if I can minimize the insturctions size to as small as possbile reducing the input tokens cost.
6. Prompt and Checks. Here the issue can be in two things prompt and guardrails. The prompt instructions might not included that to not mention the sensitve information in the response. And when the model did mentioned the sensitive data in the response the guardrail checks should block the response which it failed to do. So I will check and add guardrails for it.

### Explain it back
1. The parts, in flow order:
   UI -> Code -> Data -> Prompt -> Model -> Checks -> Logs and Evals 
2. Why the model doesn't remember, and how chat apps still seem to:
   - The model itself is stateless. It forgets the conversation once the api call is completed. So to make the model remember the previous conversation we add the conversations to the prompt while sending it to the model.
3. Three different parts that could cause a wrong answer:
   - Data, Prompt and Model.
4. Parts an AIE cares most about / parts an FDE cares most about:
   AI Engineer needs to care about building the pipeline and choosing the correct models after comparing them. And FDE takes care of how this pipeline can be effectively deployed on the customer env like connecting customers data to the pipeline and evals and logins like SSO etc etc.

---

## Lesson 0.4a · Workspace, secrets, git habits

### Try it notes
- What my own `.env` reader printed:
- What `python-dotenv` printed:

### Explain it back
1. Virtual environment, and why one per project:
It a workspace for that particular project which holds the certain packages with the exact mentioned versions. Each project get its own because when we change a version of a project it won't effect the other projects (like getting crashed etc)
2. `pyproject.toml` vs `uv.lock`; what goes in git, what never does:
pyproject.toml contains the packages used in this project and the uv.lock contains extra details of the packages like exact versions. Both files go in to git and venv/ and .env never goes into git
3. Why keys never go in code/git; first thing to do if one leaks:
Because all the code and git can be seen by other people if the repo is in public and they can use the token which get us more cost. If I push a key, I would firstrevoke that key completly and delete that commit in the repo and generate a new key and put it in the .env file and then make sure that .env is mentioned in the .gitignore
4. Two things `python-dotenv` handled that mine didn't:
It handled all the edge cases like no key, no value string, blank like and secret etc.

---

## Lesson 0.4b · First LLM call

### Try it notes
- My cost line (raw):
- My cost line (SDK):
- With `max_tokens=50`, stop_reason was:

### Explain it back
1. The 3 headers and what each is for:
     1. "x-api-key" is for sending the api key
     2. "anthropic-version" is for telling which version to use
     3. "content-type": "application/json" tells the request body type
 
2. Input vs output tokens; which costs more; my cost calculation:
   Input tokens are the ones when we send as prompt and output tokens are the models thinking and output generated tokens count. output tokens costs more. I calculated using the formuar (input_tokens * input_tokens_cost/1_000_000) + (output_tokens * output_tokens_cost/1_000_000)

3. Two things the SDK did for me; one thing it hid:
   It loaded and used the api key by itself and aslo it handled the headers by itself. It hid the URL, the headers, the raw JSON, and automatic retries.

4. What `stop_reason: "max_tokens"` means and what an app should do:
   It means the max output tokens limit is reached and the model stopped due to that reason. The might need to increase the max_tokens count or changes the prompt such that it uses less thinking power and output tokens. 

---

## Lesson 1.1 · Data, features, labels

### Your-turn notes
- My 2 extra features, and which differed most:
- ① vs ② test table results:

### Explain it back
1. One message: its label and 3 of its features:

2. Why features must be numbers:

3. The strongest spam clue in my table, and how I can tell:

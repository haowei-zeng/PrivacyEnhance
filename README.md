uvicorn app:app --host 127.0.0.1 --port 7070 --reload
uvicorn process_server:app --host 127.0.0.1 --port 5050 --reload

Then you can run the LLM_Input in Chatgpt or other websites to detect.

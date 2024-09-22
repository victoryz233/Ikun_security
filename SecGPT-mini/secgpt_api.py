# coding:utf-8
import json
import time
from queue import Queue
from threading import Thread

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用跨域支持

# 检查设备是否可用
device = "cuda" if torch.cuda.is_available() else "cpu"

# 固定加载模型和tokenizer
base_model = "C:\\Bin\\Study\\研究生\\研三\\华为杯\\SecGPT-mini\\models"  # 将此处替换为你具体的模型路径
tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_model, device_map=device, trust_remote_code=True)

def reformat_sft(instruction, input):
    if input:
        prefix = (
            "Below is an instruction that describes a task, paired with an input that provides further context. "
            "Write a response that appropriately completes the request.\n"
            "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
        )
    else:
        prefix = (
            "Below is an instruction that describes a task. "
            "Write a response that appropriately completes the request.\n"
            "### Instruction:\n{instruction}\n\n### Response:"
        )
    prefix = prefix.replace("{instruction}", instruction)
    prefix = prefix.replace("{input}", input)
    return prefix

@app.route("/")
def home():
    return "Welcome to SecGPT API. Use /api/evaluate for interactions."

@app.route("/api/evaluate", methods=["POST"])
def evaluate_api():
    # 从请求中获取参数
    data = request.json
    instruction = data.get("instruction", "")
    temperature = data.get("temperature", 0.1)
    top_p = data.get("top_p", 0.75)
    max_new_tokens = data.get("max_new_tokens", 128)
    repetition_penalty = data.get("repetition_penalty", 1.1)

    if not instruction:
        return jsonify({"error": "Instruction is required"}), 400

    prompt = reformat_sft(instruction, "")
    inputs = tokenizer(prompt, return_tensors="pt")

    if device == "cuda":
        input_ids = inputs["input_ids"].cuda()
    else:
        input_ids = inputs["input_ids"]

    # 调整生成参数
    temperature = max(0, min(1, temperature))
    top_p = max(0, min(1, top_p))
    max_new_tokens = max(1, min(2000, max_new_tokens))
    repetition_penalty = max(1, min(5, repetition_penalty))

    # 使用同步生成
    generation_config = dict(
        temperature=temperature,
        top_p=top_p,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        repetition_penalty=repetition_penalty
    )

    try:
        output_1 = model.generate(input_ids=input_ids, **generation_config)
        output_2 = model.generate(input_ids=input_ids, **generation_config)
        response_1 = tokenizer.decode(output_1[0], skip_special_tokens=True)
        response_2 = tokenizer.decode(output_2[0], skip_special_tokens=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(instruction, response_1, response_2)

    return jsonify({"response_1": response_1, "response_2": response_2})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)

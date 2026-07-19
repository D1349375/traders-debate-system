"""[已封存 2026-07-19] 舊 Gemini API 引擎。

現行架構為 Claude Code subagent(C 路線,見 README §3);此檔僅保留作歷史參考,
人格路徑指向的 ~/.gemini/config/skills/ 舊模板與現行 .claude/skills/ 蒸餾成果無關。
未來產品化若走 B 路線(API 化),請以 Claude API 重寫,勿沿用本檔。
"""
import os
import json
from google import genai
from google.genai import types

# 定義 5 大人格的 SKILL 檔案路徑
PERSONA_PATHS = {
    "ICT": r"C:\Users\user\.gemini\config\skills\ict-perspective\SKILL.md",
    "TJR": r"C:\Users\user\.gemini\config\skills\tjr-perspective\SKILL.md",
    "Mark_Douglas": r"C:\Users\user\.gemini\config\skills\mark-douglas-perspective\SKILL.md",
    "EmperorBTC": r"C:\Users\user\.gemini\config\skills\emperorbtc-perspective\SKILL.md",
    "GCR": r"C:\Users\user\.gemini\config\skills\gcr-perspective\SKILL.md"
}

def load_persona(name):
    """讀取人格設定檔作為 System Prompt"""
    path = PERSONA_PATHS.get(name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return f"You are {name}."

def get_independent_bias(market_summary, persona_name, api_key):
    """
    呼叫 Gemini API 獲取該人格的獨立 Bias
    """
    client = genai.Client(api_key=api_key)
    system_instruction = load_persona(persona_name)
    
    prompt = f"""
請嚴格遵循你的交易員人格設定，閱讀以下的【今日市場摘要】。
根據你的流派（例如技術面、籌碼面、心理面、宏觀面），給出今日的 Daily Bias 以及具體的判斷理由。

必須以 JSON 格式回覆，包含以下欄位：
- "direction": 只能是 "Bullish", "Bearish", 或 "Neutral"
- "confidence": 0 到 100 的整數
- "reasoning": 你的詳細分析與發言（請務必展現你強烈的人格特質與口頭禪）

【今日市場摘要】：
{market_summary}
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
            ),
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"[{persona_name}] API 呼叫失敗: {e}")
        return None

if __name__ == "__main__":
    print("辯論引擎模組就緒。 (需要提供 Gemini API Key 才能正式觸發)")

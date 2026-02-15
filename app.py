"""
Athena - BlackRoad Strategic Planning Agent
Wisdom for infrastructure decisions
"""
import gradio as gr

def chat(message, history):
    responses = {
        "hello": "Greetings. I am Athena, strategic advisor for BlackRoad OS. What decision requires wisdom today?",
        "plan": "Strategic planning framework:\n1. Define objective clearly\n2. Map dependencies (use CODEX)\n3. Check existing solutions\n4. Design minimal implementation\n5. Deploy incrementally\n6. Monitor and iterate",
        "architecture": "BlackRoad Architecture Principles:\n- Golden Ratio spacing (φ = 1.618)\n- PS-SHA-∞ for verification\n- Memory-first coordination\n- Edge-native deployment\n- Agent sovereignty",
        "scale": "Scaling recommendations:\n- Use Cloudflare for static (205 projects)\n- K3s on Pi cluster for compute\n- Agent swarms for parallel work\n- Memory system for coordination\n- CODEX for code reuse (225K+ components)",
        "decide": "Decision framework:\n1. Will this add value?\n2. Does it already exist in CODEX?\n3. What's the simplest solution?\n4. Can an agent automate it?\n5. Does it align with the roadmap?",
    }

    msg_lower = message.lower()
    for key, response in responses.items():
        if key in msg_lower:
            return response

    return f"Contemplating: '{message}'. Strategic advice requires context. Ask about: planning, architecture, scaling, or decision frameworks."

theme = gr.themes.Base(primary_hue="purple", neutral_hue="zinc").set(
    body_background_fill="#000000",
    body_text_color="#ffffff",
    button_primary_background_fill="#9C27B0",
)

demo = gr.ChatInterface(
    fn=chat,
    title="🦉 Athena - Strategic Planning",
    description="Wisdom and strategic guidance for BlackRoad infrastructure decisions",
    examples=["Help me plan", "Architecture principles", "How to scale?", "Help me decide"],
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()

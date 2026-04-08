import re

class GhostwriterEnv:
    def __init__(self):
        self.forbidden_words = ["very", "really", "basically", "just"]
        self.target_tone = "Professional"

    def calculate_reward(self, current_text: str, task_id: str) -> float:
        score = 1.0
        # Penalty for forbidden words
        for word in self.forbidden_words:
            if word in current_text.lower():
                score -= 0.2
        
        # Reward for professional length/structure
        if len(current_text) > 50:
            score += 0.1
            
        return max(0.0, min(1.0, score))

    def step(self, action: Action):
        # 1. Apply the action to the text
        # 2. Calculate reward
        reward_score = self.calculate_reward(action.suggested_text, "easy")
        # 3. Return (observation, reward, done, info)
        return Observation(...), reward_score, action.action_type == "submit", {}

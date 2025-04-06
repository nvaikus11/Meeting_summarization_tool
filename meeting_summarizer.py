import openai
import tkinter as tk
from tkinter import scrolledtext

# Initialize OpenAI client
client = openai.OpenAI(api_key="Add API Key Here")

# Function to get summary from GPT-4
def generate_summary():
    transcript = input_text.get("1.0", tk.END).strip()
    if not transcript:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a meeting transcript.")
        return

    prompt = f"""
    Here is a meeting transcript:
    {transcript}

    Generate a structured summary with the following sections:
    - Summary: A short overview of the meeting.
    - What Went Well: Key positives from the discussion.
    - What Did Not Go Well: Areas that need improvement.
    - Improvement Suggestions: Actionable ideas or recommendations.
    """

    try:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Generating summary, please wait...")
        root.update_idletasks()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that summarizes meetings."},
                {"role": "user", "content": prompt}
            ]
        )

        summary = response.choices[0].message.content

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, summary)

    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

# Create the Tkinter UI
root = tk.Tk()
root.title("Meeting Summarization Tool")
root.geometry("800x500")

# Input Textbox
input_label = tk.Label(root, text="Enter Meeting Transcript:", font=("Arial", 12))
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
input_text.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Summary", command=generate_summary, font=("Arial", 12), bg="lightblue")
generate_button.pack(pady=10)

# Output Textbox
output_label = tk.Label(root, text="Summary Output:", font=("Arial", 12))
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
output_text.pack()

# Run the Tkinter App
root.mainloop()


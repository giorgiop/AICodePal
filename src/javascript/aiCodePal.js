const axios = require('axios');

async function getChatGPTSuggestion(codeSnippet) {
  const apiKey = 'YOUR_API_KEY';
  const url = 'https://api.openai.com/v1/engines/davinci-codex/completions';
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`
  };
  const data = {
    prompt: `Improve the following JavaScript code: ${codeSnippet}`,
    max_tokens: 50,
    n: 1,
    stop: null,
    temperature: 0.7,
  };

  try {
    const response = await axios.post(url, data, { headers });
    const suggestion = response.data.choices[0].text;
    return suggestion.trim();
  } catch (error) {
    console.error('Error:', error);
  }
}


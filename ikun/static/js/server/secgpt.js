<script>
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    // 添加消息到聊天框
    function addMessage(content, isUser) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(isUser ? 'user-message' : 'ai-message');
        messageElement.textContent = `${isUser ? 'You: ' : 'SecGPT: '}${content}`;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // 错误处理
    function addErrorMessage(error) {
        const errorElement = document.createElement('div');
        errorElement.classList.add('error-message');
        errorElement.textContent = `Error: ${error}`;
        chatMessages.appendChild(errorElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // 获取 AI 响应
    async function getAIResponse(instruction) {
        try {
            const response = await fetch('http://127.0.0.1:7777/api/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    instruction: instruction,  // 将用户输入作为指令发送
                    temperature: 0.7,         // 控制生成文本的多样性（可选）
                    top_p: 0.9,               // 控制生成的随机性（可选）
                    max_new_tokens: 128       // 限制生成内容的最大长度（可选）
                }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data.response_1;  // 获取 AI 返回的第一个响应
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }

    // 处理发送按钮点击事件
    async function handleSend() {
        const message = userInput.value.trim();  // 获取并清理用户输入
        if (message === '') return;

        addMessage(message, true);  // 在界面上显示用户输入
        userInput.value = '';  // 清空输入框
        sendButton.disabled = true;  // 禁用按钮，防止多次点击

        try {
            const response = await getAIResponse(message);  // 调用 API 获取响应
            addMessage(response, false);  // 显示 AI 响应
        } catch (error) {
            addErrorMessage('Failed to get response from SecGPT');  // 处理错误
        } finally {
            sendButton.disabled = false;  // 恢复按钮
        }
    }

    // 为发送按钮和回车键绑定事件
    sendButton.addEventListener('click', handleSend);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });
</script>

<script lang='ts'>
    import ChatBubble from "$lib/components/ChatBubble.svelte";
    import { chat } from '$lib/ipc';

    let message = '';

    let chatMessages = [];
    async function sendMessage() {
        if (message.trim() !== '') {
            
            chatMessages =[...chatMessages, {text: message, sender: 'sender'}]
            const response = await chat(message);
            chatMessages =[...chatMessages, {text: response, sender: 'receiver'}]
        }
        message = '';
    }
</script>

<style>
    .bubble-container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .message-box {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        margin-top: 20px;
        background: white;
        padding: 10px;
    }
    .message-box input {
        flex-grow: 1;
        margin-right: 10px;
    }
</style>


<div class="bubble-container">
    {#each chatMessages as chatMessage (chatMessage.text)}
        <ChatBubble text={chatMessage.text} sender={chatMessage.sender}></ChatBubble>
    {/each}
</div>

<div class="message-box">
    <input bind:value={message} type="text" placeholder="Type a message" on:keydown={(e) => e.key === 'Enter' && sendMessage()} />
    <button on:click={sendMessage}>Send</button>
</div>
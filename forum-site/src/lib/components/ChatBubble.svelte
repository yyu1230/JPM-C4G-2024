<script lang='ts'>
    export let text : string;
    export let sender : 'receiver' | 'sender';
</script>

<style>
    .bubble {
        display: inline-block;
        width: auto;
        max-width: 40%;
        padding: 10px 20px;
        margin: 10px 0;
        border-radius: 20px;
        color: white;
    }
    .bubble.sender {
        background-color: #0b93f6;
        align-self: flex-end;
        text-align: right;
        color: black;
    }
    .bubble.receiver {
        background-color: green;
        align-self: flex-start;
        text-align: left;
        color: black;
    }
</style>

<div class="bubble {sender}">
    {text}
</div>
<br>
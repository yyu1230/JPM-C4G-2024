<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
	import { postPost } from "$lib/ipc";
    import { v4 as uuidv4 } from 'uuid';


    let post : ForumPost = {
        title: "",
        content: "",
        id: "",
        author : "You",
        created : ""
    };
    let showPost = false;

    function closePost() {
        showPost = false;
    }

    async function submitPost() {
        post.id = uuidv4();
        closePost();
        await postPost(post);
        post.content = ""
        post.title = ""
    }
</script>

<style>
    .forum-post {
        width: 100%;
        background-color: grey;
        padding: 20px;
        box-sizing: border-box;
        overflow: auto;
    }

    .title-input {
        width: 100%;
        margin-bottom: 10px;
    }
    .content-input {
        width: 100%;
        height: 200px;
        resize: vertical;
    }

    .centered-button {
        position: absolute;
        left: 50%;
        
    }
</style>
{#if showPost}
    <div class="forum-post">
        <input class="title-input" type="text" bind:value={post.title} placeholder="Title" />
        <textarea class="content-input" bind:value={post.content} placeholder="Content"></textarea>
        <button type="submit" on:click={submitPost} >Submit</button>
    </div>
{:else}
    <button class="centered-button" on:click={() => showPost = true}>Create Post</button>
{/if}


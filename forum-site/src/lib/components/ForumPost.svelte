<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import type { ForumComment } from "$lib/bindings/ForumComment";
	import { onMount } from "svelte";
    export let post : ForumPost;

    let comments : Promise<ForumComment[]>;

    onMount(async () => {
        try {
            const response = await fetch(`http://comments:5000/comments/${post.id}`, {
                method : 'GET'
            });
            comments = response.json();
        }
        catch (error) {
            console.error(error);
        }
    });
</script>
<style>
    .forum-post {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: white;
        padding: 20px;
        box-sizing: border-box;
        overflow: auto;
    }

    .close-button {
        position: absolute;
        top: 20px;
        right: 20px;
        cursor: pointer;
    }
</style>

{#await comments}
    <p>Loading...</p>
{:then comments}
    <div class="forum-post">
        <div class="close-button" on:click>X</div>
        <h1>{post.title}</h1>
        <p>{post.content}</p>
    </div>
    {#each comments as comment}
        <div>
            <div>{comment.author}</div>
            <div>{comment.content}</div>
        </div>
    {/each}
{:catch error}
    <p>{error}</p>
{/await}
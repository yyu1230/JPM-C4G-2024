<script lang="ts">
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import type { ForumComment } from "$lib/bindings/ForumComment";
    import { onMount } from "svelte";
    import CommentDisplay from "$lib/components/CommentDisplay.svelte";
    import { postComment } from "$lib/ipc.js";
    export let data;
    let formPost : ForumPost = data.post
    let comments : ForumComment[] = data.comments


    let newComment = '';
    async function handleCommentSubmit() {
        await postComment(formPost.id, newComment);
        comments = [...comments , {
            id : formPost.id,
            author : "You",
            content : newComment,
            created : new Date().toISOString()
        }];
        newComment = '';
    }
</script>

<style>
    .title {
        text-align: center;
        background-color: #f0f0f0;
        padding-top: 10px;
    }
    .content {
        background-color: #e0e0e0;
        padding-left: 20px;
    }
    form {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    textarea {
        width: 100%;
        resize: vertical;
    }
    button {
        margin-top: 0px;
    }
</style>

<h1 class="title">{formPost.title}</h1>
<p class="content">{formPost.content}</p>

<form on:submit|preventDefault={handleCommentSubmit}>
    <textarea bind:value={newComment} placeholder="Write a comment..."></textarea>
    <button type="submit">Post Comment</button>
</form>

{#each comments as comment}
    <CommentDisplay comment={comment} />
{/each}

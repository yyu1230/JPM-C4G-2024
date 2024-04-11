<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
    export let post : ForumPost;
    import { goto } from '$app/navigation';



    function navigateToPost() {
        goto(`forum/posts/${post.id}`);
    }
</script>


<style>
    .forum-head {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        height: 50px;
        border: 1px solid #ccc;
        background-color: grey;
        margin-bottom: 10px;
        margin-top: 10px;
    }

    .title {
        font-weight: bold;
    }

    .preview {
        color: blue;
    }

    .info {
        text-align: right;
    }
</style>

<div class="forum-head">
    <div>
        <div class="title" on:click={navigateToPost}>{post.title}</div>
        <div class="preview">{post.content.substring(0, 50)}...</div>
    </div>
    <div class="info">
        <div>{post.author}</div>
        <div>{post.created}</div>
    </div>
</div>
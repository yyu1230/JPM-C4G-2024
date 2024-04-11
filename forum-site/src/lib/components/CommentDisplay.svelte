<script lang='ts'>
    import type { ForumComment } from "$lib/bindings/ForumComment";
    export let comment : ForumComment;
</script>

<div class="comment">
    <h2>{comment.author}</h2>
    <p>{comment.content}</p>
</div>

<style>
    .comment {
        margin-bottom: 20px;
    }
    .comment h2 {
        font-size: 1.2em;
        margin-bottom: 10px;
    }
</style>
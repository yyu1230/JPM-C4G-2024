<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
	import CreateForumPost from "$lib/components/CreateForumPost.svelte";
    import ForumHead  from "$lib/components/ForumHead.svelte";
	import { fetchPosts } from "$lib/ipc";
	import { get } from "svelte/store";

    let posts = fetchPosts();


</script>

{#await posts}
    <p>Loading...</p>
{:then posts}
    {#each posts as post}
        <ForumHead post={post} />
    {/each}
    
    <CreateForumPost></CreateForumPost>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}

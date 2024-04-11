<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import ForumHead  from "$lib/components/ForumHead.svelte";
    import { forumPosts } from '$lib/stores/store';
	import { get } from "svelte/store";

    let dummyPosts : ForumPost[] = [{
        title: "Example Title",
        content: "Example Content",
        id : "1",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "Wow I love JPM",
        content: "So we have a lot of content here we're trying to put a realllllllyy long text to see what it loks like when I do ayayayayayayayay",
        id : "2",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "sokmethig else ig guess",
        content: "Example Content",
        id : "3",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "Wowzers hey reviewer reading this code",
        content: "Example Content",
        id : "4",
        author : "Author",
        created : "Now",
    }, 
    ];

    forumPosts.set(dummyPosts);


</script>


{#each get(forumPosts) as post}
    <ForumHead post={post} />
{/each}

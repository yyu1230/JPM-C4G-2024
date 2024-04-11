<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import ForumHead  from "$lib/components/ForumHead.svelte";
    let exampleFormPosts : ForumPost[] = [{
        title: "Example Title",
        content: "Example Content",
        id : "",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "Wow I love JPM",
        content: "So we have a lot of content here we're trying to put a realllllllyy long text to see what it loks like when I do ayayayayayayayay",
        id : "",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "sokmethig else ig guess",
        content: "Example Content",
        id : "",
        author : "Author",
        created : "Now",
    }, 
    {
        title: "Wowzers hey reviewer reading this code",
        content: "Example Content",
        id : "",
        author : "Author",
        created : "Now",
    }, 



    ];


</script>


{#each exampleFormPosts as post}
    <ForumHead post={post} />
{/each}

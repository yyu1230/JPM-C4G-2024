Landing page


<script>
    import { fetchComments, fetchPosts } from "$lib/utils";
    async function handleClick() {
        try {
            const response = await fetch("http://127.0.0.1:5000/hello", {
                method : 'POST'
            });
            const data = await response.json();
            console.log(data);

        }
        catch (error) {
            console.error(error);
        }
    }
    async function handlePosts() {
        try {
            let postID = "ID1"
            const response = await fetch(`http://127.0.0.1:5000/comments/${postID}`, {
                method : 'GET'
            });
            const data = await response.json();
            console.log(data);

        }
        catch (error) {
            console.error(error);
        }
    }

    async function handleComments() {
        try {
            const response = await fetch("http://127.0.0.1:5000/posts", {
                method : 'GET'
            });
            const data = await response.json();
            console.log(data);

        }
        catch (error) {
            console.error(error);
        }
    }
</script>

<button on:click={() => {fetchComments("792c0ca3-b488-49ef-8fcf-0d96094643ed")}}>Click me</button>
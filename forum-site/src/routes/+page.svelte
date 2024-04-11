Landing page


<script>
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

<button on:click={handlePosts}>Click me</button>
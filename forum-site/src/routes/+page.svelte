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
</script>

<button on:click={handleClick}>Click me</button>
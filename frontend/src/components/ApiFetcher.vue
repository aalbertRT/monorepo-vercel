<script setup>
    import { ref } from 'vue';
    const data = ref(null);
    const loading = ref(false);
    const error = ref(null);
    const fetchData = async () => {
        loading.value = true;
        error.value = null;
        data.value = null;
        try {
            console.log(import.meta.env.VITE_API_URL)
            const response = await fetch(import.meta.env.VITE_API_URL);
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            const result = await response.json();
            data.value = JSON.stringify(result, null, 2); // Convert response to a formatted JSON string
        } catch (err) {
            error.value = err.message;
        } finally {
            loading.value = false;
      }
    };


</script>

<template>
    <div class="general">
        <button @click="fetchData">Fetch</button>
        <div v-if="loading">Loading...</div>
        <div v-if="error">{{ error }}</div>
        <pre v-if="data">{{ data }}</pre>
    </div>
</template>

<style scoped>

.general {
    text-align: center;
}
</style>
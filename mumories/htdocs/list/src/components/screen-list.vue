<script setup>
    import { computed, onMounted, ref } from 'vue';
    import { useStore } from '@/store.js';
    const store = useStore();
    const projects = computed(() => store.projects);
</script>

<template>
    <h1>Mumories</h1>

    <h2>Here are some mumories</h2>

    <p v-if="projects.length === 0">loading...</p>

    <ul v-if="projects">
        <li v-for="project in projects">
            <small>#{{project.index}}: {{project.en_on_show}}</small>

            <a v-bind:href="'#' + project.index">
                {{project.en_index_title}}
            </a>
        </li>
    </ul>
</template>
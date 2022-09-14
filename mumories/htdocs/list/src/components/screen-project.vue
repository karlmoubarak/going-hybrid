<script setup>
    import { computed, onMounted, ref } from 'vue';
    import { useStore } from '@/store.js';
import ElAudioSnippet from './el-audio-snippet.vue';
    const store = useStore();
    const project = computed(() => store.currentProject);

    console.log(project.value);
</script>

<template>
    <a href="#">👈 Back to overview</a>

    <h1>{{project.en_page_title}}</h1>
    <h2>{{project.en_page_subtitle}}</h2>

    <ul class="metadata">
        <li>⏰ {{project.en_show_start}}</li>
        <li>🪪 {{project.index}}</li>
        <li><a v-bind:href="project.en_link_en">Exhibition website 🇬🇧</a></li>
        <li><a v-bind:href="project.en_link_nl">Exhibition website 🇳🇱</a></li>
    </ul>

    <ElAudioSnippet
        v-if="project.audio"
        :project="project"
    />

    <img class="image" v-bind:src="project.en_index_img" />

    <article v-html="project.en_page_text"></article>
</template>

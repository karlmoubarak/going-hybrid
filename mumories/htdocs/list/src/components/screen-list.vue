<script setup>
    import ElFunctional from '@/components/el-functional.vue';
    import ElImages from '@/components/el-images.vue';
    import ElTight from '@/components/el-tight.vue';

    import { computed, onMounted, ref } from 'vue';
    import { useStore } from '@/store.js';

    const store = useStore();
    const projects = computed(() => store.projects);
    const currentView = ref('functional');

    const views = [
        'functional', 'tight', 'images'
    ];

    function setView(view) {
        currentView.value = view;
    }
</script>

<template>
    <h1>Mumories</h1>

    <p v-if="projects.length === 0">loading...</p>

    <template v-if="projects.length">
        <menu class="views">
            <button
                v-for="view in views"
                class="views__button"
                v-bind:is-selected="view === currentView ? 'is-selected' : null"
                v-on:click="setView(view)">
                {{view}}
            </button>
        </menu>

        <el-functional
            v-if="currentView === 'functional'"
            v-bind:projects="projects"></el-functional>

        <el-tight
            v-if="currentView === 'tight'"
            v-bind:projects="projects"></el-tight>

        <el-images
            v-if="currentView === 'images'"
            v-bind:projects="projects"></el-images>
    </template>
</template>
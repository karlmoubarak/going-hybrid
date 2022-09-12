<script setup>
    import ScreenList from './components/screen-list.vue';
    import ScreenProject from './components/screen-project.vue';
    import { computed, onMounted, ref } from 'vue';
    import { useStore } from '@/store.js';

    const store = useStore();

    const screen = computed(() => store.screen);

    function setHash() {
        if (!!window.location.hash) {
            const hash = window.location.hash.slice(1);
            store.setProjectIndex(hash);
        } else {
            store.deleteProjectIndex();
        }

        window.scrollTo(0, 0);
        console.log(screen.value);
    }

    onMounted(async () => {
        await store.loadProjects();
        setHash();
    });

    window.addEventListener('hashchange', () => setHash());
</script>

<template>
    <screen-list
        v-if="screen === 'list'"></screen-list>

    <screen-project
        v-if="screen === 'project'"></screen-project>
</template>

<style lang="scss" src="./scss/style.scss"></style>
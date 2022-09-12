<script setup>
    const props = defineProps({
        projects : Array
    });
</script>

<template>
    <ul class="el-tight">
        <li v-for="project in props.projects">
            <a v-bind:href="'#' + project.index">
                {{project.en_index_title}}
            </a>
        </li>
    </ul>
</template>
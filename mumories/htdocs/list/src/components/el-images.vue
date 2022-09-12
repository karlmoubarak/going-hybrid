<script setup>
    const props = defineProps({
        projects : Array
    });
</script>

<template>
    <ul class="el-images">
        <li v-for="project in props.projects">
            <a v-bind:href="'#' + project.index">
                <img v-bind:src="project.en_index_img"
                     v-bind:alt="'Image for the project ' + project.en_page_title" />
            </a>
        </li>
    </ul>
</template>
<script setup>
    const props = defineProps({
        projects : Array
    });
</script>

<template>
    <ul class="el-functional">
        <li v-for="project in props.projects">
            <small>#{{project.index}}: {{project.en_on_show}}</small>

            <a v-bind:href="'#' + project.index">
                {{project.en_index_title}}
            </a>
        </li>
    </ul>
</template>
import { getProjects } from '@/api.js';
import { defineStore } from 'pinia';

export const useStore = defineStore('data', {
    state: () => {
        return {
            projectIndex : -1,
            projects : []
        };
    },

    getters : {
        currentProject() {
            if (this.projectIndex > -1 && this.projects.length) {
                return this.projects.find((p) => p.index === this.projectIndex);
            } else {
                return false;
            }
        },

        screen() {
            console.log('projectIndex', this.projectIndex);
            return this.projectIndex > -1 ? 'project' : 'list';
        },
    },

    actions : {
        deleteProjectIndex() {
            this.projectIndex = -1;
        },

        async loadProjects() {
            console.log('loading projects');
            const projects = await getProjects();
            console.log(projects);
            this.projects = projects;
            console.log('projects loaded');
        },

        setProjectIndex(index) {
            this.projectIndex = index;
        }
    }
});

import { getJson } from 'donot';
import { API_ENDPOINT } from './const.js';

export async function getProjects() {
    const url = `${API_ENDPOINT}/?action=get-projects&format=json`;
    return await getJson(url);
}
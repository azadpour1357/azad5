import axios from 'axios';

const API_URL = 'http://backend:5000';

export const searchDocuments = async (query) => {
  try {
    const response = await axios.post(`${API_URL}/search`, { query });
    return response.data;
  } catch (error) {
    console.error('Error fetching search results:', error);
    throw error;
  }
};
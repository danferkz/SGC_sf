// store/index.js
import { createStore } from 'vuex';
import sessions from './modules/sessions';
import axios from 'axios';


export default createStore({
    modules: {
        sessions
    }
});
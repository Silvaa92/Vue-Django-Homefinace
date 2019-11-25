import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import {
    ADD_TRANSACTION,
    REMOVE_TRANSACTION,
    SET_TRANSACTIONS
} from './mutation-types.js'

const HTTP = axios.create({
    baseURL:'http://127.0.0.1:8000/'
})

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        transactions: [],
    },
    getters: {
        transactions: state => state.transactions
    },
    mutations: {
        [ADD_TRANSACTION] (state, transaction) {
            state.transactions.push(transaction);
        },
        [REMOVE_TRANSACTION] (state, transaction) {
            state.transactions.splice(state.transactions.indexOf(transaction), 1);
        },
        [SET_TRANSACTIONS] (state, transactions) {
            state.transactions = transactions;
        }
    },
    actions: {
        async createTransaction ({ commit }, transactionData) {
            const response = await HTTP.post('transactions/', transactionData);
            if (response.status === 201) {
                commit(ADD_TRANSACTION, response.data)
            }
        },
        async deleteTransaction({ commit }, transaction) {
            const response = await HTTP.delete(`/transactions/${transaction.id}/`);
            if (response.status === 201) {
                commit(REMOVE_TRANSACTION, response.data)
            }
        },
        async getTransactions ({ commit }) {
            const response = await HTTP.get('transactions/');
            if (response.status === 200) {
                commit(SET_TRANSACTIONS, response.data.results)
            }
        }
    }
})
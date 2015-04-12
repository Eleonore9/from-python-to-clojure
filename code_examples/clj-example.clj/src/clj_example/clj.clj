(ns clj-example.clj
  (:require [clojure.string :as str])
  (:gen-class))


(def data ;; Get data from the csv
  (str/split-lines (slurp "resources/data.csv")))

(def headers ;; Get column headers
  (str/split (first data) #","))

(defn list-data []
  "Builds a list of maps with the data."
  (mapv #(zipmap headers
                 (str/split % #","))
        (rest data)))

(defn transform-keys
  "Turns keys into keywords and deals with spaces."
  [str-key]
  (-> str-key
      clojure.string/lower-case
      (clojure.string/replace #" " "-")
      keyword))

(defn keywordize-keys-with-space
  "Recursively transforms all map keys from strings to keywords and deals
  with the space for 2 words keys."
  [data-map]
  (->> data-map
       (mapv #(hash-map (transform-keys (key %))
                       (val %)))
       (reduce merge)))

(defn -main
  "List humanitarian data from 2014."
  []
  (->> (list-data)
       (mapv #(keywordize-keys-with-space %))
       (keep #(if (> (read-string (:total-affected %)) 0) %))
       (mapv #(select-keys % [:country-name :disaster-subgroup]))
       (map #(format "%s was affected by a %s disaster" (:country-name %)
                     (:disaster-subgroup %)))))

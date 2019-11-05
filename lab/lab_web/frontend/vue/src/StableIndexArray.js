class StableIndexArray extends Array {
    constructor(...values) {
        super();
        values.forEach(x => this.push(x))
    }
    push(value) {
        if (!(value instanceof Object)) {
            let type = typeof value,
                cls = window[type[0].toUpperCase() + type.slice(1)];
            if (cls) {
                value = new cls(value);
            }
        }
        super.push(Object.assign(value, { idx: this.length, __deleted: false }));
    }
    existing() {
        let values = [];
        for (let i = 0; i < this.length; ++i) {
            if (this[i].__deleted === false) {
                values.push(Object.assign({}, this[i]));
                delete values[values.length - 1].__deleted;
            }
        }
        return values;
    }
    remove(element) {
        if (!("idx" in element)) {
            return;
        }
        for (let i = 0; i < this.length; ++i) {
            if (this[i].idx == element.idx) {
                this[i].__deleted = true;
            }
        }
    }
}
(window || {}).StableIndexArray = StableIndexArray;
export default StableIndexArray;
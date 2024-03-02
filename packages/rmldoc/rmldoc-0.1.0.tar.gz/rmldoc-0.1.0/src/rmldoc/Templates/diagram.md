- **RDF triples pattern**
```mermaid
%%{ init : { "theme" : "forest", "flowchart" : { "curve" : "linear" }}}%%
flowchart LR
{% for po in pom -%}
    S["{{ subject }}"] -->|"{{ po['predicate'] }}"| object{{ loop.index }}("{{ po['object'] }}")
{%+ endfor %}    
``` 


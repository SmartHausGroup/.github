/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    // Getting started
    {
      type: 'category',
      label: 'Getting started',
      collapsed: false,
      items: ['intro', 'about'],
    },
    // Framework (why)
    {
      type: 'category',
      label: 'Framework',
      items: ['thesis/framework'],
    },
    // RFS (core tech)
    {
      type: 'category',
      label: 'Resonant Field Storage (RFS)',
      link: { type: 'doc', id: 'rfs/overview' },
      items: [
        'rfs/overview',
        'rfs/field-theory',
        {
          type: 'category',
          label: 'Use Cases',
          link: { type: 'doc', id: 'rfs/use-cases/overview' },
          items: [
            'rfs/use-cases/overview',
            'rfs/use-cases/incident-memory',
            'rfs/use-cases/rag-proofs',
            'rfs/use-cases/code-intelligence',
            'rfs/use-cases/compliance-legal',
            'rfs/use-cases/research-knowledge',
            'rfs/use-cases/pharmaceutical',
          ],
        },
      ],
    },
    // Methodology
    {
      type: 'category',
      label: 'Methodology',
      items: ['mathematical-autopsy/overview'],
    },
    // Archetypes (what we build)
    {
      type: 'category',
      label: 'Archetypes',
      items: [
        'archetypes/tai',
        'archetypes/aiva',
        'archetypes/mge',
      ],
    },
  ],
};

module.exports = sidebars;
